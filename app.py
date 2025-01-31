import streamlit as st
from rembg import remove
from PIL import Image
import io

def remove_background(image):
    """Remove o fundo de uma imagem usando rembg."""
    output = remove(image)
    return output

def main():
    st.title("Remoção de Fundo de Imagem")

    uploaded_file = st.file_uploader("Carregue uma imagem", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        try:
            # Abre a imagem com PIL
            image = Image.open(uploaded_file)
            st.image(image, caption="Imagem Original", width=300)

            # Remove o fundo
            with st.spinner("Removendo fundo..."):
                output_image = remove_background(image)

            # Mostra a imagem sem fundo
            st.image(output_image, caption="Imagem sem Fundo", width=300)

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