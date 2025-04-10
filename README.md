
# 🗺️ Streamlit_App_GIS_Clustering_FCM_PSO

This is a **Streamlit-based web application** for performing **geospatial clustering** using **Fuzzy C-Means (FCM)** optimized with **Particle Swarm Optimization (PSO)**. In addition to spatial clustering, the app includes a basic **blog dashboard** to post, view, and manage news or articles related to your data insights.

---
]## 🚀 Features

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

| GIS Clustering View | Blog View |
|---------------------|-----------|
| ![Map](screenshots/map.png) | ![Blog](screenshots/blog.png) |

---

## 📌 Requirements

- Python 3.8+
- Internet connection (for loading Mapbox tiles)
- Shapefile and structured Excel dataset

---

## 📬 Contact

Built with ❤️ by [Your Name].  
For questions or collaborations, reach out via [your.email@example.com].

---

## 📝 License

This project is licensed under the MIT License.
