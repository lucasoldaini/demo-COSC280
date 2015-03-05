function emptySearchBox(){
    sb = document.getElementById("searchbox");
    if (sb.value=="") {
        document.getElementById("submit-search-button").value="Search";
    }

}
function setDefaultValueSearchBox () {
    sb = document.getElementById("searchbox");
    if (sb.value=="") {
        document.getElementById("submit-search-button").value="View All";
    };
}

setDefaultValueSearchBox();
