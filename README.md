## Setup Environment - Shell/Terminal
1. Update sistem operasi dan paket:
    ```bash
    sudo apt update
    sudo apt upgrade
    ```

2. Install `virtualenv` jika belum terpasang:
    ```bash
    pip install virtualenv
    ```

3. Buat direktori proyek dan masuk ke dalamnya:
    ```bash
    mkdir ~/my_project
    cd ~/my_project
    ```

4. Buat dan aktifkan virtual environment:
    ```bash
    virtualenv myenv
    source myenv/bin/activate
    ```

## Install Dependencies
1. Install library yang dibutuhkan:
    ```bash
    pip install pandas==2.1.4
    pip install matplotlib==3.8.0
    pip install seaborn==0.13.0
    pip install streamlit==1.30.0
    ```

## Run Streamlit Dashboard
1. Jalankan dashboard menggunakan Streamlit:
    ```bash
    streamlit run dashboard.py
    ```

2. Akses dashboard melalui browser di alamat:
    ```
    http://localhost:8501
    ```
