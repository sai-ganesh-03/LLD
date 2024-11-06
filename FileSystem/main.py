from File import File
from Directory import Directory


if __name__=="__main__":
    movies_dir=Directory("Movies")
    kalki_file=File("Kalki")
    
    comedy_movies=Directory("Comedy Movies")
    hera_pheri_movie=File("Hera Pheri")
    
    comedy_movies.add_nodes(hera_pheri_movie)
    
    movies_dir.add_nodes(kalki_file)
    movies_dir.add_nodes(comedy_movies)
    
    movies_dir.ls()