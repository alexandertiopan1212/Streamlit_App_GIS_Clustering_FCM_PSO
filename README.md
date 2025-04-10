
# 🗺️ Streamlit_App_GIS_Clustering_FCM_PSO

This is a **Streamlit-based web application** for performing **geospatial clustering** using **Fuzzy C-Means (FCM)** optimized with **Particle Swarm Optimization (PSO)**. In addition to spatial clustering, the app includes a basic **blog dashboard** to post, view, and manage news or articles related to your data insights.

---

## 🚀 Features

### 🧠 GIS Clustering Module
- Reads `.shp` shapefile and Excel datasets containing geographic and indicator data.
- Visualizes clustering results with interactive **Plotly Choropleth Mapbox**.
- Implements **Fuzzy C-Means (FCM)** clustering, enhanced with **PSO optimization**.
- Evaluation metrics: **Davies-Bouldin Score** and **Silhouette Score**.

### 📰 Blog & News Management
- Create, view, and delete posts in a simple blog system.
- Uses **SQLite** as the backend database.
- Blog cards styled with HTML templates for a clean layout.

---

## 🧱 Folder Structure

```
.
├── app.py                # Main Streamlit app
├── pso_clustering.py     # FCM-PSO clustering logic
├── particle.py           # PSO particle behavior
├── db_functions.py       # Blog-related SQLite functions
├── data.db               # SQLite database
├── dataset/              # Folder for uploaded Excel files
├── gadm36_IDN_2.shp      # Shapefile for Indonesia's regions
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/Streamlit_App_GIS_Clustering_FCM_PSO.git
cd Streamlit_App_GIS_Clustering_FCM_PSO
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

---

## 📊 Screenshots


![image](https://github.com/user-attachments/assets/19db95cd-1e0d-4b57-b5b3-7207402ddbed)
![image](https://github.com/user-attachments/assets/1e544102-baee-41d8-8a94-58ffcd2eb8bb)
![image](https://github.com/user-attachments/assets/3647b249-3fcb-430a-9570-6addf4ecb94e)
![image](https://github.com/user-attachments/assets/5d8a5e17-dc8c-4cf1-b86d-f971ef080661)
![image](https://github.com/user-attachments/assets/f07fdde7-8da0-48cc-97b2-e4c872c14cea)
![image](https://github.com/user-attachments/assets/14f275e9-6431-4733-a832-64f08446653a)
![image](https://github.com/user-attachments/assets/3b8f019e-38b7-45c9-8f30-5018b92a4b52)


---

## 📌 Requirements

- Python 3.8+
- Internet connection (for loading Mapbox tiles)
- Shapefile and structured Excel dataset

---

## 📬 Contact

Built with ❤️ by **Alexander Tiopan**  
📧 Email: alexandertiopan1212@gmail.com  
💼 LinkedIn: [linkedin.com/in/alexander-tiopan-85215117b](https://www.linkedin.com/in/alexander-tiopan-85215117b)

---

## 📝 License

This project is licensed under the MIT License.
