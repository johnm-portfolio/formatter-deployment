// Made by John McNally

const body = document.getElementsByTagName("body")[0];
const table = document.getElementById("symbol-table");
const tableBody = table.getElementsByTagName("tbody")[0];
const tableHead = table.getElementsByTagName("thead")[0];
const themeButton = document.getElementById("theme-button");
const themeButtonImg = themeButton.children[0];
themeButton.addEventListener("click", changeTheme);

const filterDropdown = document.getElementById('filter');
const tableRows = document.querySelectorAll('tbody tr');

function changeTheme(){
    let themeStyle = "dark";
    if (body.className == "dark-theme-main") {
        themeStyle = "light";
    }
    else {
        themeStyle = "dark";
    }
    body.className = `${themeStyle}-theme-main`;
    tableBody.className = `${themeStyle}-theme-table-body`;
    tableHead.className = `${themeStyle}-theme-table-heading`;
    themeButton.className = `${themeStyle}-theme-button`;
    themeButtonImg.src = `Images/${themeStyle}_theme_button_icon.png`;
}

filterDropdown.addEventListener('change', applyFilter);
function applyFilter(){
    function changeHiddenValue(row, filterValue){
        if (filterValue === 'all') {
            row.classList.remove('hidden');
        }
        else {
            if (row.classList.contains(filterValue)) {row.classList.remove('hidden');}
            else {row.classList.add('hidden');}
        }
    }
    let filterValue = filterDropdown.value;
    tableRows.forEach(function(row) {changeHiddenValue(row, filterValue);});
}

let slaurg = document.getElementsByClassName("symbol");
for (let i = 0; i < slaurg.length; i++){
    slaurg[i].addEventListener("click", function(){copyTextToClipboard(slaurg[i])})
}
// slaurg.forEach(function(symbol){
//     symbol.addEventListener("click", function(){copyTextToClipboard(element)});
// })

function copyTextToClipboard(element){
    console.log(element.textContent);
    navigator.clipboard.writeText(element.textContent);
    alert(`"${element.textContent}" copied to clipboard`);
}