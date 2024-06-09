import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import base64

# Load the dataset
file_path = 'C:\\Users\\Senku Ishigami\\Desktop\\webapp\\anime-dataset-2023.csv'
anime_data = pd.read_csv(file_path)

def get_top_anime(genre, studio):
    filtered_data = anime_data[anime_data['Genres'].str.contains(genre, na=False) & anime_data['Studios'].str.contains(studio, na=False)]
    top_anime = filtered_data.sort_values(by='Score', ascending=False).head(1)
    return top_anime

def plot_top_anime(genre, studio):
    filtered_data = anime_data[anime_data['Genres'].str.contains(genre, na=False) & anime_data['Studios'].str.contains(studio, na=False)]
    top_animes = filtered_data.sort_values(by='Score', ascending=False).head(10)
    plt.figure(figsize=(10, 6))
    sns.set(style="whitegrid")
    bar_plot = sns.barplot(x='Score', y='Name', data=top_animes, palette='viridis')
    bar_plot.set_title(f'Top 10 Animes in {genre} Genre by {studio} Studio', fontsize=16)
    bar_plot.set_xlabel('Score', fontsize=14)
    bar_plot.set_ylabel('Anime', fontsize=14)
    for i in bar_plot.containers:
        bar_plot.bar_label(i, fontsize=12)
    st.pyplot(plt)

sharingan_icon_url = 'C:\\Users\\Senku Ishigami\\Desktop\\webapp\\jujutsu.png'
st.set_page_config(page_title="Anime Recommendation System", page_icon=sharingan_icon_url)

# Set background image
background_image_url = 'https://scontent.fdvo2-2.fna.fbcdn.net/v/t1.15752-9/445373076_449321637797023_6000582594042833077_n.png?_nc_cat=106&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeHIQSadmLL7GBrpen0Lylt-VB8X5-QcBqtUHxfn5BwGq8rer9e-yC7HXm7nhcZ_Qqm1c8Uc_yE7ap0HLc4TuBbY&_nc_ohc=lgmD43tKL68Q7kNvgFvbnIV&_nc_ht=scontent.fdvo2-2.fna&oh=03_Q7cD1QHwBkn0eDK2vGRPG0hY7vjBERFMg0fNaF4Ju2KW8M60FQ&oe=668D4F55'
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({background_image_url});
        background-size: contain;
        background-attachment: fixed;
        background-repeat: no-repeat;
        background-position: center;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.title("OtakuX: Animeverse Guide㊙")
st.header("Find your Hollow Purple🫴🟣")

# Select Genre
genres = sorted(set(genre for sublist in anime_data['Genres'].dropna().str.split(', ') for genre in sublist))
selected_genre = st.selectbox("Select Genre☯", genres)

# Select Studio
studios = sorted(set(studio for sublist in anime_data['Studios'].dropna().str.split(', ') for studio in sublist))
selected_studio = st.selectbox("Select Studio⛩️", studios)

if selected_genre and selected_studio:
    top_anime = get_top_anime(selected_genre, selected_studio)
    
    if not top_anime.empty:
        st.subheader("Top Recommended Anime")
        st.write(f"**Name:** {top_anime['Name'].values[0]}")
        st.write(f"**Score:** {top_anime['Score'].values[0]}")
        st.write(f"**Genres:** {top_anime['Genres'].values[0]}")
        st.write(f"**Synopsis:** {top_anime['Synopsis'].values[0]}")
        st.write(f"**Type:** {top_anime['Type'].values[0]}")
        st.write(f"**Episodes:** {top_anime['Episodes'].values[0]}")
        st.write(f"**Aired:** {top_anime['Aired'].values[0]}")
        st.image(top_anime['Image URL'].values[0])
        
        # Plot chart for top animes
        st.subheader("Top 10 Animes in Selected Genre and Studio")
        plot_top_anime(selected_genre, selected_studio)
    else:
        st.write("No anime found for the selected genre and studio.")

@st.cache_data
def get_img_as_base64(file):
    if os.path.exists(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    else:
        st.error(f"File not found: {file}")
        return None

# Use relative path
img_path = os.path.join(os.path.dirname(__file__), 'sharingan.jpg')
img = get_img_as_base64(img_path)

if img:
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] > .main {{
    background-image: url("https://scontent.fdvo2-1.fna.fbcdn.net/v/t1.15752-9/442727244_351799994285762_8137414755917419837_n.png?_nc_cat=101&ccb=1-7&_nc_sid=5f2048&_nc_eui2=AeEeDmrEYoCpl60Jn90qkfXWWHJBQbXlk7NYckFBteWTs2y8M05pQKTt6TPGqU6T1gCWtc7KFzKrKcKyDa4AA-Mn&_nc_ohc=Z0KtWGejALwQ7kNvgHoZq2Q&_nc_ht=scontent.fdvo2-1.fna&oh=03_Q7cD1QG8Hyn19Cvk05cUm1OWW6BehmkSEgn8mG2ax_q_1PyI4Q&oe=668D428D");
    background-size: 30%;
    background-position: top right;
    background-repeat: no-repeat;
    background-attachment: local;
    }}

    [data-testid="stSidebar"] > div:first-child {{
    background-image: url("data:image/png;base64,{img}");
    background-position: center; 
    background-repeat: no-repeat;
    background-attachment: fixed;
    }}

    [data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
    }}

    [data-testid="stToolbar"] {{
    right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("うちはイタチ")

with st.container():
    st.header("▬▬ι═══════ﺤ")
    st.markdown(
        "Web application designed using Streamlit for a recommendation system: OtakuX Animeverse Guide㊙. It is a recommendation system that gives services to anime enthusiasts. Users can filter out whichever genre or studio they would like to find top-rated titles within these dropdown options. It has an interface with an exciting icon and image that augments the aesthetic looks of the screen. The application also involves data visualization with bar plots as one of the plots for representing the top anime in their selected genre and studio, which is quite appealing to the user. Such a level of intuitive design and fluid functionality will ensure OtakuX throws users right into that melodramatic world of anime, quickly guiding them down the path toward a new favorite series."
    )






