import streamlit as st
from rembg import remove
from PIL import Image
import io
import numpy as np
import os

def remove_background(image):
    """Remove o fundo de uma imagem usando rembg."""
    output = remove(image)
    return output

def main():
    # Define o caminho da imagem
    logo_path = "logo.png"  # Altere para "images/logo.png" se estiver em uma subpasta

    # Verifica se o arquivo existe
    if os.path.exists(logo_path):
        # Carrega a imagem do logo
        logo = Image.open(logo_path)
    
        # Exibe o logo na barra lateral
        st.sidebar.image(logo, width=150)  # Ajuste o valor de 'width' para o tamanho desejado
    else:
        st.sidebar.error(f"Erro: Arquivo de imagem não encontrado em {logo_path}")

    # Adiciona o link do GitHub na barra lateral
    st.sidebar.markdown(
        """
        [Código no GitHub](https://github.com/eduardosucco/remove-bg)
        """,
        unsafe_allow_html=True # Necessary for using markdown tags
    )

    st.title("Remoção de Fundo de Imagem")

    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            # Abre a imagem com PIL
            image = Image.open(uploaded_file)

            # Remove o fundo
            with st.spinner("Removendo fundo..."):
                output_image = remove_background(image)
            
            # Convert PIL image to numpy array
            image_np = np.array(image)
            output_image_np = np.array(output_image)

            # Cria as colunas
            col1, col2 = st.columns(2)

            # Exibe a imagem original na primeira coluna
            with col1:
                st.image(image_np, use_container_width=True)
                st.caption("Imagem Original")

            # Exibe a imagem sem fundo na segunda coluna
            with col2:
                st.image(output_image_np, use_container_width=True)
                st.caption("Imagem sem Fundo")

            # Download da imagem
            buffered = io.BytesIO()
            output_image.save(buffered, format="PNG")
            
            st.download_button(
                label="Baixar imagem sem fundo",
                data=buffered.getvalue(),
                file_name="imagem_sem_fundo.png",
                mime="image/png"
            )
            
        except Exception as e:
            st.error(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    main()