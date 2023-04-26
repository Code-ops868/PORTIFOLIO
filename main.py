#from streamlit_option_menu import option_menu
import streamlit as st
#import components.v1 as con
#import pywhatkit as pwt




##############################################################
st.set_page_config(page_title="CODE-MIND",page_icon="cod.png")
#PARA SELEÇAO DE MENUS################################
st.header(":orange[MENU]")
Lista_de_Menu=st.selectbox("---",options=['HOME','SOBRE','SERVIÇOS','CURSOS','APLICATIVOS','CONTACTOS'])



# CRIANDO O SIDEBAR LATERAL########################################################################################
with st.sidebar:
    Logotipo ="cod.png"
  
    st.image(Logotipo)
    st.title(":orange[TRANSFORMANDO IDEIAS EM INFORMAÇÕES TECNOLÓGICAS!]")
    st.title(":orange[Cell:]")
    st.write("(+258)-876587356")
    st.write("(+258)-845756134")
    QRCODEE="mind.png"
    st.image(QRCODEE)


    st.title(":orange[Cidade de Nampula]")


if Lista_de_Menu=="HOME":
    st.header(":orange[BEM-VINDO A CODE-MIND]")
    Imagem="PG.png"
    st.image(Imagem)
#CRIANDO COLUNAS
col1, col2, col3  = st.columns(3)
# PÁGINA SERVIÇOS
if Lista_de_Menu=="SERVIÇOS":
    with col1:
        st.header(":orange[API]")
        API="api.png"
        st.image(API)
        st.write("Por exemplo, imagine que você está usando um aplicativo de previsão do tempo em seu celular. Esse aplicativo precisa de informações atualizadas sobre o clima em diferentes locais para funcionar corretamente. Em vez de coletar todas essas informações por conta própria, o aplicativo usa uma API de um provedor de dados climáticos para buscar os dados necessários.API é uma forma de integrar diferentes sistemas de software e permitir que eles troquem informações de forma padronizada e segura")


    with col2:
        st.header(":orange[CRIAÇAO DE QRCODES]")
        CODIGO="QRC.jpg"
        st.image(CODIGO)
        st.write("Os QR Codes são amplamente utilizados em marketing, publicidade e comércio eletrônico, pois permitem que as pessoas acessem informações rapidamente e facilmente, sem precisar digitar manualmente. Eles também são comumente usados em ingressos de eventos, cartões de visita digitais e até mesmo em aplicações de autenticação de dois fatores em contas online.")
        
       
    with col3:
        st.header(":orange[AUTOMAÇAO DE TAREFAS]")
        Automa="automaçao.jpg"
        st.image(Automa)
        st.write("Automação de tarefas é quando usamos computadores para realizar tarefas repetitivas de forma automática. É como ter um ajudante eletrônico que pode executar tarefas para você sem precisar que você faça manualmente.\n Por exemplo, imagine que você precisa enviar um e-mail para várias pessoas todos os dias. Isso pode ser cansativo e demorado, certo? Mas se você criar um programa que envie automaticamente esses e-mails para você, isso seria automação de tarefas!")
    col4, col5, col6 =st.columns(3)
    with col4:
        st.header(":orange[ANÁLISE DE DADOS]")
        DADOS = "grafico.png"
        st.image(DADOS)
        st.write("Quando fazemos análise de dados, organizamos as informações em tabelas, gráficos ou outros formatos para entender melhor o que os dados estão nos dizendo.\n A análise de dados nos ajuda a entender melhor as informações que temos e a tomar decisões mais informadas com base nessas informações. É como se fosse uma ferramenta para nos ajudar a encontrar respostas e soluções para nossas perguntas!")
        st.write(":orange[Ligue já para saber mais]")
    with col5:
# WEBSCRAPING=======================================
        st.header(":orange[WEBSCRAPING]")
        Das_Imagem ="Web.png"
        st.image(Das_Imagem)
        st.write("Web scraping é a técnica de extrair dados de sites de forma automatizada. É comumente usada para coletar informações de sites públicos, como preços de produtos, informações de contato e avaliações de clientes. Esses dados podem ser usados para análise de mercado, pesquisa de concorrência e outras finalidades comerciais")
        st.write(":orange[Ligue já para saber mais]")
    with col6:
        st.header(":orange[DESENVOLVIMENTO WEB]")
        Foto ="dev4.png"
        st.image(Foto)
        st.write("Criamos sites, aplicativos e sistemas que são acessíveis pela internet. Esses sistemas podem ser acessados através de navegadores web, como Chrome, Firefox ou Safari e outros")
        st.write(":orange[Ligue já para saber mais]")
# PÁGINA SOBRE
if Lista_de_Menu=="SOBRE":
    st.header(":orange[Quem Sou]")
    st.write("Sou o criador da marca :red[CODE-MIND], programador apaixonado por criar soluções digitais incríveis.Ofereço serviços de desenvolvimento web, incluindo a criação de sites e dashboards personalizados, desenvolvimento de aplicativos para Android e desktop, design gráfico além de oferecer :red[cursos de programação] para aqueles que desejam aprender a codificar. O meu objetivo é fornecer soluções digitais inovadoras que atendam às necessidades específicas do cliente, sempre com um toque pessoal e atenção aos detalhes. Estou comprometido em oferecer o melhor serviço possível e estou sempre procurando maneiras de superar as expectativas de meus clientes.")
    Foto_Perfil ="bra.png"
    st.image(Foto_Perfil)
    st.write(":orange[======_Abrao Alberto_======   ]")
if Lista_de_Menu=="CONTACTOS":
    st.header(":orange[Entre em Contacto comigo enviando um E-mail]")
    Menu ='''
        <form action="https://formsubmit.co/apoiocodeminde@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="nome" placeholder="Informe o seu Nome" required>
            <input type="email" placeholder="Seu Email!" required>
            <textarea name="message" placeholder="Envie sua Mensagem Aqui!" rows="10" required></textarea>
            <button type="submit">ENVIAR</button>
            
        
        
        
        </form>
    
    '''
    
#FUNÇAO PARA INTEGRAR O CSS E HTML
    st.markdown(Menu, unsafe_allow_html=True)
    def Local(file):
        with open(file) as f:
            st.markdown(f"<style>{f.read()}</syle>", unsafe_allow_html=True)
    Local('style.css')
if Lista_de_Menu=="APLICATIVOS":
    st.header(":orange[Página ainda em Desenvolvimento]")
    st.file_uploader(label="Baixar Aplicativo")
    st.download_button(label="Baixar Aplicativos", data="")
if Lista_de_Menu =="CURSOS":
    st.header("")
    col1, col2, col3 = st.columns(3)
    with col1:
        
        st.subheader(':green[Programação com a linguagem Python]')
        st.write("Python é uma linguagem extremamente eficiente: seus programas farão mais\ncom menos linhas de código, se comparados ao que muitas outras linguagens exigiriam.\n A sintaxe de Python também ajudará você a escrever\num código limpo. Seu código será fácil de ler, fácil de depurar, fácil de se intender\n e de expandir, quando comparado com outras linguagens.") 
        st.write("As pessoas usam Python para muitos propósitos: criar jogos, construir aplicações web, resolver problemas de negócios e desenvolver ferramentas\n internas em todo tipo de empresas interessantes. Python também é\n intensamente usada em áreas científicas para pesquisa acadêmica e trabalhos")
        st.write(":orange[Ligue já para saber mais]")
    with col2:
        st.subheader(":orange[HTML e CSS para Desenvolvimento Web]")
        st.write(":black[Desenvolvimento web é o processo de criação de sites, aplicativos e sistemas que são acessíveis pela internet. Esses sistemas podem ser acessados através de navegadores web, como Chrome, Firefox ou Safari, e geralmente são criados usando tecnologias como HTML, CSS, JavaScript e diversas outras linguagens de programação de back-end, como PHP, Python, Ruby, Java, entre outra]")
        st.write(":orange[Ligue já para saber mais]")
    with col3:
        st.subheader(":green[Kivy e Kivymd para Desenvolvimento Mobile]")
        st.write("Os aplicativos móveis podem ter diversas finalidades, desde jogos e entretenimento até ferramentas de produtividade e utilitários. A programação mobile envolve a criação de interfaces de usuário otimizadas para dispositivos móveis, que geralmente possuem telas menores do que as de computadores desktop.")
        
hiden ='''
<style>
#MainMenu {visibility:hidden;}
header {visibility:hidden;}
footer {visibility:hidden}
</style>
'''
st.markdown(hiden,unsafe_allow_html=True)
        
