# BTh11_Trieblaengenwachstum

In diesem Repository `BTh11_Trieblaengenwachstum` werden Skripts für die Verarbeitung und Analyse von Punktwolken und Bildern abgelegt. Die Skripts werden für die Bachelor Thesis 11 im Jahr 2025 erstellt und verwendet.

Das Environment `BTh11_TLW`enthält folgende Bibliotheken:

- Visualisierung und Analyse von Punktwolken (`pyvista`, `open3d`, `vtk`, `pyntcloud`)
- Geodatenverarbeitung (`geopandas`, `pyproj`, `shapely`, `pyogrio`)
- Webvisualisierung und Dashboards (`plotly`, `dash`, `flask`)
- Klassifikation und Statistik (`scikit-learn`, `numpy`, `pandas`, `scipy`)
- Interaktive Widgets und Notebooks (`ipywidgets`, `jupyterlab`, `ipython`)

## 1. Installation unter Windows (Bash)

### 1.1 Neues Conda-Environment erstellen

```bash
conda create -n BTh11_TLW python=3.11
```

### 1.2 Environment aktivieren

```bash
conda activate BTh11_TLW
```

### 1.3 Installation der Kernpakete über Conda

```bash
conda install -c conda-forge pip geopandas matplotlib numpy pandas scikit-learn scipy shapely pyproj laspy vtk open3d pyvista dash flask plotly ipywidgets ipython jupyterlab stringcase tqdm retrying pyogrio
```

### 1.4 Zusätzliche Pakete über pip installieren

```bash
pip install \
  asttokens==3.0.0 \
  attrs==25.3.0 \
  blinker==1.9.0 \
  certifi==2025.1.31 \
  charset-normalizer==3.4.1 \
  click==8.1.8 \
  colorama==0.4.6 \
  comm==0.2.2 \
  ConfigArgParse==1.7 \
  contourpy==1.3.1 \
  cycler==0.12.1 \
  decorator==5.2.1 \
  executing==2.2.0 \
  fastjsonschema==2.21.1 \
  fonttools==4.56.0 \
  idna==3.10 \
  importlib_metadata==8.6.1 \
  ipython_pygments_lexers==1.1.1 \
  itsdangerous==2.2.0 \
  jedi==0.19.2 \
  Jinja2==3.1.6 \
  joblib==1.4.2 \
  jsonschema==4.23.0 \
  jsonschema-specifications==2024.10.1 \
  jupyter_core==5.7.2 \
  jupyterlab_widgets==3.0.13 \
  kiwisolver==1.4.8 \
  MarkupSafe==3.0.2 \
  matplotlib-inline==0.1.7 \
  narwhals==1.31.0 \
  nbformat==5.10.4 \
  nest-asyncio==1.6.0 \
  parso==0.8.4 \
  pillow==11.1.0 \
  platformdirs==4.3.7 \
  pooch==1.8.2 \
  prompt_toolkit==3.0.50 \
  pure_eval==0.2.3 \
  Pygments==2.19.1 \
  pyntcloud==0.3.1 \
  pyparsing==3.2.1 \
  python-dateutil==2.9.0.post0 \
  pytz==2025.1 \
  pywin32==310 \
  referencing==0.36.2 \
  requests==2.32.3 \
  rpds-py==0.23.1 \
  scooby==0.10.0 \
  setuptools==77.0.3 \
  six==1.17.0 \
  stack-data==0.6.3 \
  threadpoolctl==3.6.0 \
  traitlets==5.14.3 \
  typing_extensions==4.12.2 \
  tzdata==2025.1 \
  urllib3==2.3.0 \
  wcwidth==0.2.13 \
  Werkzeug==3.0.6 \
  widgetsnbextension==4.0.13 \
  zipp==3.21.0
```

## 2. Hinweise für die Installation

- Die Installation verwendet `conda-forge`
- Es wird eine Kombination aus `conda` und `pip` verwendet
- Diese Anleitung setzt eine funktionierende Anaconda/Miniconda-Installation auf Windows voraus

## 3. Repository Struktur
Das Repository `BTh11_Trieblaengenwachstum` ist modular aufgebaut und gliedert sich in Teilschritte der Punktwolkenanalyse, die der quantitativen Erfassung des Trieblängenwachstums mittels UAV-Photogrammetrie und LiDAR dienen:

```text
📁 01_PointCloud_Attributes           
    → Prüfen von Attributen photogrammetrischer Punktwolken

📁 02_PointCloud_Clipping            
    → Zuschneiden von Punktwolken basierend auf Geometrie (BBox) und Höhe

📁 03_TPF_Statistics                 
    → Statistische Analyse der Tie Point Filtering-Effekte auf Punktwolkenqualität

📁 04_FrameExtraction_Video         
    → Extraktion von Einzelbildern für Spezialauswertungen

📁 05_Software_Comparison           
    → Vergleich verschiedener SfM-Softwares (Metashape vs. Drone2Map)

📁 06_UAV_Comparison                
    → Vergleich der Punktwolkenergebnisse von DJI Mini 3 Pro und Phantom 4 Pro V2

📁 07_Check_PG-PointCloud_Completeness  
    → Untersuchung der Rekonstruktionsvollständigkeit im Vergleich zur TLS-Referenz

📁 08_PointCloud_2_Skeleton         
    → Vorbereitung und Datenhaltung für Skelettierungsansätze (z. B. TreeQSM, AdTree)

📁 09_CraneCam_ZHAW_Comparison     
    → Vergleich von UAV-Punktwolken mit Bilddaten des CraneCam-Systems (ZHAW)

📁 10_ImageAlignment_Testing       
    → Einfluss unterschiedlicher Matching-/Alignment-Parameter auf die Rekonstruktion

📁 11_Camera_TestChart             
    → Vergleich der Kameras anhand ISO-12233-Charts zur Beurteilung der Bildqualität

📁 12_CameraCalibration            
    → Analyse und Visualisierung der internen Kamerakalibrierungsparameter

📁 13_Voxel_based_pc_analysis      
    → Voxelisierung von Punktwolken zur volumetrischen Analyse der Baumkronen

📁 14_TreeQSM-Zylinder_to_Skeleton 
    → Transformation von QSM-Zylindermodellen in Skelettstrukturen (Triebebene)

📁 15_Calendar_Vis                 
    → Visualisierung der Aufnahme- und Messzeitpunkte im Projektverlauf

📁 16_Metadata_Statistics          
    → Analyse der EXIF-Daten zur Nachvollziehbarkeit der UAV-Aufnahmen

📁 17_ShootLengthGrowth_Vis       
    → Visualisierung gemessener Trieblängen (Messstreifen, Kurvenverlauf pro Baumart)

📁 18_Timeline_RMSE_ERROR         
    → Zeitreihenvergleich der RMSE-Werte (3D-Fehler, Pixelabweichung)

📁 99_old                         
    → Archivierte Skripts
```
