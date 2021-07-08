from pdf2image import convert_from_path
 
images = convert_from_path("C:/Users/Codex/Desktop/imagem/m02.pdf")
 
for i in range(len(images)):
   
     # Salvar as páginas como imagens no pdf
    images[i].save('page'+ str(i) +'.PNG', 'PNG')

    #http://blog.alivate.com.au/poppler-windows/
    #https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/
    #https://pdf2image.readthedocs.io/en/latest/installation.html