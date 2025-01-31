import streamlit as st
from rembg import remove
from PIL import Image
import io
import numpy as np

def remove_background(image):
    """Remove o fundo de uma imagem usando rembg."""
    output = remove(image)
    return output

def main():
    # Configura o nome da aba do navegador
    st.set_page_config(
        page_title="✨ Easy Remove BG",
        page_icon="✂️",
    )

    # Adiciona uma descrição do projeto na barra lateral
    st.sidebar.title("✂️ Easy Remove BG")
    st.sidebar.markdown(
        """
        Este é um aplicativo web simples que permite remover o fundo de imagens usando a biblioteca `rembg`.
        
        **Instruções:**
        1.  ⬆️ Carregue uma imagem (PNG, JPG ou JPEG).
        2.  ✨ O aplicativo irá remover o fundo automaticamente.
        3.  💾 Baixe a imagem sem fundo.
        """
    )

    # Adiciona o link do GitHub na barra lateral
    st.sidebar.markdown(
        """
        [🔗 Código no GitHub](https://github.com/eduardosucco/remove-bg)
        """,
        unsafe_allow_html=True
    )

    st.title("Remoção de Fundo de Imagem")

    uploaded_file = st.file_uploader("⬆️ Carregue uma imagem", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            # Abre a imagem com PIL
            image = Image.open(uploaded_file)

            # Remove o fundo
            with st.spinner("✨ Removendo fundo..."):
                output_image = remove_background(image)
            
            # Convert PIL image to numpy array
            image_np = np.array(image)
            output_image_np = np.array(output_image)

            # Cria as colunas
            col1, col2 = st.columns(2)

            # Exibe a imagem original na primeira coluna
            with col1:
                st.image(image_np, use_container_width=True)
                st.caption("🖼️ Imagem Original")

            # Exibe a imagem sem fundo na segunda coluna
            with col2:
                st.image(output_image_np, use_container_width=True)
                st.caption("🖼️ Imagem sem Fundo")

            # Download da imagem
            buffered = io.BytesIO()
            output_image.save(buffered, format="PNG")
            
            st.download_button(
                label="💾 Baixar imagem sem fundo",
                data=buffered.getvalue(),
                file_name="imagem_sem_fundo.png",
                mime="image/png"
            )
            
        except Exception as e:
            st.error(f"Erro ao processar a imagem: {e}")

if __name__ == "__main__":
    main()