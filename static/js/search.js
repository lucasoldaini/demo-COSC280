function emptySearchBox(){
    // remove default value from searchbox when user clicks (or taps) on it
    sb = document.getElementById("searchbox");
    if (sb.value=="") {
        document.getElementById("submit-search-button").value="Search";
    }

}
function setDefaultValueSearchBox () {
    // restore default value for searchbox when user leaves it and it is empty
    sb = document.getElementById("searchbox");
    if (sb.value=="") {
        document.getElementById("submit-search-button").value="View All";
    };
}

setDefaultValueSearchBox();
