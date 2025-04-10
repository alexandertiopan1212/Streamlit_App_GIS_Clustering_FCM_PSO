import pandas as pd
from pso_clustering import PSOClustering
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
import streamlit as st
import geopandas as gpd
import warnings
warnings.filterwarnings("ignore")
import geopandas as gpd
import plotly.express as px
from db_functions import *

# Layout for Blog Templates
html_temp = """
<div style="background-color:{};padding:10px;border-radius:10px">
<h1 style="color:{};text-align:center;">Simple Blog </h1>
</div>
"""
title_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
<h6>Author:{}</h6>
<br/>
<br/> 
<p style="text-align:justify">{}</p>
</div>
"""
article_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<h6>Author:{}</h6> 
<h6>Post Date: {}</h6>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
<br/>
<br/>
<p style="text-align:justify">{}</p>
</div>
"""
head_message_temp ="""
<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
<h4 style="color:white;text-align:center;">{}</h1>
<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
<h6>Author:{}</h6> 
<h6>Post Date: {}</h6> 
</div>
"""
full_message_temp ="""
<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
<p style="text-align:justify;color:black;padding:10px">{}</p>
</div>
"""




def main():
    st.title(':blue[FCM-PSO]')
    st.header('_:blue[GIS Data Processing using Fuzzy C-Means with PSO Optimization]_')
    st.write("""
Aplikasi ini digunakan untuk mengelompokkan data cluster berdasarkan data geografis
             """)
    
    # Session handling
    if 'login_accepted' not in st.session_state:
        st.session_state.login_accepted = 0
    
    if 'data' not in st.session_state:
        st.session_state.data = pd.DataFrame()
    
    if 'data_ori' not in st.session_state:
        st.session_state.data_ori = pd.DataFrame()
    
    if 'username' not in st.session_state:
        st.session_state.username = ''

    if 'password' not in st.session_state:
        st.session_state.password = ''
    


    # Sidebar initiation
    st.sidebar.title("Menu")
    menu = st.sidebar.selectbox("Home", ["Default", "Akun", "Upload Data", "Training FCM-PSO"])
    menu2 = st.sidebar.selectbox("Report", ["Default", "Evaluasi"])
    menu3 = st.sidebar.selectbox("News and Information", ["Default", "Home NEWS & INFO", "View Posts","Add Posts","Manage Blog"])

    if menu == "Akun" and menu2 == "Default" and menu3 == "Default":
        st.subheader("Selamat Datang. Silahkan Masuk.")
        st.session_state.username = st.text_input("Username")
        st.session_state.password = st.text_input("Password", type="password")
        login_button = st.button("Masuk")

        if st.session_state.username == "user" and st.session_state.password == "123" and login_button:
            st.success(f"Selamat Datang {st.session_state.username}. Akun Berhasil Masuk. Silahkan Akses Menu Lain.")
            st.session_state.login_accepted = 1

    if menu == "Upload Data" and menu2 == "Default" and menu3 == "Default":
        if st.session_state.login_accepted == 1:
            uploaded_file = st.file_uploader("Choose a file")
            if uploaded_file is not None:
                #read excel
                st.session_state.data=pd.read_excel(uploaded_file, engine='openpyxl')
                st.session_state.data_ori=pd.read_excel(uploaded_file, engine='openpyxl')
                st.dataframe(st.session_state.data)
                
                frame = "gadm36_IDN_2.shp"

                df = gpd.read_file(frame)
                df = df.to_crs("WGS84")
                df_new = df[['NAME_2', 'geometry']]
                df_new = df_new.loc[df_new['NAME_2'].isin(st.session_state.data['Wilayah'].values)].reset_index()[['NAME_2', 'geometry']]
                data2= st.session_state.data.drop(['Wilayah'], axis=1)
                df_new2 = pd.concat([df_new, data2], axis = 1).dropna()


                df_new2 = df_new2.set_index("NAME_2")
                fig = px.choropleth_mapbox(
                    data_frame = df_new2, # Using the id as index of the data
                    geojson = df_new2.geometry,                # The geometry
                    locations = df_new2.index,                 # The index of the data
                    color = 'Stunting',
                    mapbox_style = 'open-street-map',
                    center = dict(lat = -8.6, lon = 121),
                    zoom = 5)

                st.plotly_chart(fig, use_container_width=True)

        if st.session_state.login_accepted == 0:
            st.subheader("Anda Belum Login. Silahkan Login atau Daftar Terlebih Dahulu.")



    if menu == "Training FCM-PSO" and menu2 == "Default" and menu3 == "Default":
        if st.session_state.login_accepted == 1:
            st.subheader("Masukkan Input Parameter:")
            n_clusters = st.number_input("Jumlah Cluster", min_value=2, step=1)
            n_particles = st.number_input("Jumlah Partikel", min_value=2, step=1)
            iteration = st.number_input("Jumlah Iterasi", min_value=2, step=1)
            
            if st.button("Mulai Training"):
                le = LabelEncoder()
                le.fit(st.session_state.data['Wilayah'])
                le.transform(st.session_state.data['Wilayah'])
                st.session_state.data['Wilayah'] = le.transform(st.session_state.data['Wilayah'])

                columns = st.session_state.data.columns
                scalarModel = StandardScaler()
                st.session_state.data = scalarModel.fit_transform(st.session_state.data)
                st.session_state.data = pd.DataFrame(st.session_state.data , columns = columns )

                st.session_state.data = st.session_state.data.values
                data_to_train = st.session_state.data.copy()
                pso = PSOClustering(n_clusters, n_particles, data=data_to_train)
                res = pso.start(iteration)
                cluster_result = res[0]

                
                st.session_state.davies_bo = []
                for item in res[1]:
                    st.session_state.davies_bo.append(item[0])

                st.session_state.shill = []
                for item in res[1]:
                    st.session_state.shill.append(item[1])
                
                data_t = pd.concat([st.session_state.data_ori, pd.DataFrame({"cluster": cluster_result[-1]})], axis=1)

                st.write(data_t)

                frame = "gadm36_IDN_2.shp"

                df = gpd.read_file(frame)
                df = df.to_crs("WGS84")
                df_new = df[['NAME_2', 'geometry']]
                df_new = df_new.loc[df_new['NAME_2'].isin(data_t['Wilayah'].values)].reset_index()[['NAME_2', 'geometry']]
                data2= data_t.drop(['Wilayah'], axis=1)
                df_new2 = pd.concat([df_new, data2], axis = 1).dropna()

                df_new2 = df_new2.set_index("NAME_2")
                fig = px.choropleth_mapbox(
                    data_frame = df_new2, # Using the id as index of the data
                    geojson = df_new2.geometry,                # The geometry
                    locations = df_new2.index,                 # The index of the data
                    color = 'cluster',
                    mapbox_style = 'open-street-map',
                    center = dict(lat = -8.6, lon = 121),
                    zoom = 5)

                st.plotly_chart(fig, use_container_width=True)

        if st.session_state.login_accepted == 0:
            st.subheader("Anda Belum Login. Silahkan Login atau Daftar Terlebih Dahulu.")


    if menu2 == "Evaluasi" and menu == "Default" and menu3 == "Default":
        if st.session_state.login_accepted == 1:
            df_ = pd.DataFrame({"David Bouldin Score": st.session_state.davies_bo,
                                "Shilloute Score": st.session_state.shill})
            df_['size'] = 10

            # Create scatter plot
            fig = px.scatter(df_,
            x = df_.index,
            y = "David Bouldin Score",
            title = f"David Bouldin Score",
            size = "size")
                    
            # Plot
            st.plotly_chart(fig, use_container_width=True)

            # Create scatter plot
            fig = px.scatter(df_,
            x = df_.index,
            y = "Shilloute Score",
            title = f"Shilloute Score",
            size = "size")
                    
            # Plot
            st.plotly_chart(fig, use_container_width=True)

        if st.session_state.login_accepted == 0:
            st.subheader("Anda Belum Login. Silahkan Login atau Daftar Terlebih Dahulu.")

    if menu3 == "Home NEWS & INFO" and menu == "Default" and menu2 == "Default":
        create_table()
        st.subheader("Home")
        result = view_all_notes()
        for i in result:
            b_author = i[0]
            b_title = i[1]
            b_article = str(i[2])[0:30]
            b_post_date = i[3]
            st.markdown(title_temp.format(b_title,b_author,b_article,b_post_date),unsafe_allow_html=True)

    if menu3 == "View Posts" and menu == "Default" and menu2 == "Default":
        st.subheader("View Posts")

        all_titles = [i[0] for i in view_all_titles()]
        postlist = st.sidebar.selectbox("Posts",all_titles)
        post_result = get_blog_by_title(postlist)
        for i in post_result:
            st.markdown(head_message_temp.format(i[1],i[0],i[3]),unsafe_allow_html=True)
            st.markdown(full_message_temp.format(i[2]),unsafe_allow_html=True)

    if menu3 == "Add Posts" and menu == "Default" and menu2 == "Default":
        st.subheader("Add Your Article")
        blog_title = st.text_input('Enter Post Title')
        blog_author = st.text_input("Enter Author Name",max_chars=50)
        blog_article = st.text_area("Enter Your Message",height=200)
        blog_post_date = st.date_input("Post Date")
        if st.button("Add"):
            add_data(blog_author,blog_title,blog_article,blog_post_date)
            st.success("Post::'{}' Saved".format(blog_title))

    if menu3 == "Manage Blog" and menu == "Default" and menu2 == "Default":
        st.subheader("Manage Blog")
        result = view_all_notes()
        # st.write(result)
        clean_db = pd.DataFrame(result,columns=["Author","Title","Article","Date"])
        st.dataframe(clean_db)
        unique_list = [i[0] for i in view_all_titles()]
        delete_by_title =  st.selectbox("Select Title",unique_list)
        if st.button("Delete"):
            delete_data(delete_by_title)
            st.warning("Deleted: '{}'".format(delete_by_title))

if __name__ == '__main__':
    main()