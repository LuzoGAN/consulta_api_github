import requests
import streamlit as st

BASE_URL = "https://api.github.com"

def selecionarUsuario(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def ui():
    st.markdown(r'<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-9ndCyUaIbzAi2FUVXJi0CjmCapSmO7SnpJef0486qhLnuZ2cdeRhO02iuK6FUUVM" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Consulta Github')
    username = st.text_input('Insira o username de usuário do Githib')

    if st.button('Buscar'):
        infoUsuario =   selecionarUsuario(username)
        if infoUsuario is not None:
            st.markdown(f"""
                <div class="card" style="width: 18rem;">
                    <img src="{infoUsuario['avatar_url']}" class="card-img-top" alt="...">
                    <div class="card-body">
                        <h5 class="card-title">{infoUsuario['login']}</h5>
                        <p class="card-text">{infoUsuario['bio']}</p>
                        <a href="{infoUsuario['html_url']}" style="color: white; text-decoration: none" class="btn btn-primary">Ver Perfil</a>
                    </div>
                </div>
                """, unsafe_allow_html=True
            )

ui()