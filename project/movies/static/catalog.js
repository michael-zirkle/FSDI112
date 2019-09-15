function loadData(){

    $.ajax({
        url:'http://127.0.0.1:8000/api/movies',
        type: 'GET',
        success: function(res){
            console.log('data from server: ', res);
            displayMovies(res.objects);
        },
        error: function(error){
            console.error("ERROR ON GET", error);
        }


    });
}

function displayMovies(list) {
    var table = $("#tblCatalog > tbody");
    for(var i = 0; i <list.length; i++){
        var movie = list[i];
        var row = 
        '<tr> 
            <td>${movie.id}</td>
            <td>${movie.title}</td>
            <td>${movie.release_year}</td>
            <td>${movie.price}</td>
        </tr>';
        table.append(row);
    }

}

function init(){
    loadData();
}

window.onload = init;
