const numberWithCommas = (x) => {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
}

const sorter = (array, sortBy) => {
    function GetSortOrder(prop) {    
        return function(a, b) {    
            if (a[prop] > b[prop]) {    
                return 1;    
            } else if (a[prop] < b[prop]) {    
                return -1;    
            }    
            return 0;    
        }    
    }array.sort(GetSortOrder(sortBy))
    return array;
}

const getHTML = (countryArr) => {
    var html = new String();
    countryArr.forEach((country, count) => {
        html += `<tr>
            <th>${count+1}</th>
            <th><a id="NameDescAnch" onclick="openModal(${country.id})">${country.name}</a></th>
            <th>${country.capital}</th>
            <th>${country.region}</th>
            <th>${country.subRegion}</th>
            <th>${numberWithCommas(country.population)}</th>
            <th>${country.languages}</th>
            <th>${country.currency}</th>
            <th>${country.code}</th>
        </tr>`;
    });return html;
}
const resetDiffElem = (elemId) => {
    var options = document.querySelectorAll(`#${elemId} option`);
    for (var i = 0, l = options.length; i < l; i++) {
        options[i].selected = options[i].defaultSelected;
    }
}
const resetAll = () => {
    fetch("/all-data").then(res=>res.json()).then(countries => {
        document.getElementById("tableContent").innerHTML = getHTML(countries);
        resetDiffElem("filterBy")
        resetDiffElem("sortBy")
        resetDiffElem("FilterValue")
    })
}
const openModal = (id) => {
    var html = new String();
    fetch(`/all-data?id=${id}`).then(res=>res.json()).then(country=>{
        document.getElementById("exampleModalLabel").innerHTML = country.name;
        html += `<tr>
                    <th><img src="${country.flag}" height="25px", width="25px"></img></th>
                    <th>${numberWithCommas(country.area)} KM<sup>2</sup></th>
                    <th>${country.nativeName}</th>
                </tr>`
        document.getElementById("modalTableBody").innerHTML = html;
        $("#descModal").modal();
    })
}

window.onload = () => {
    fetch("/all-data").then(res=>res.json()).then(countries => {
        document.getElementById("allTableData").value = JSON.stringify(countries);
    })
}
document.getElementById("filterBy").oninput = function(e){
    if ( e.target.value === "region"){
        var html = `<option value="null">--select a value--</option>`
        fetch("/all-regions").then(res=>res.json()).then(regions => {
            regions.forEach(region => {
                html += `<option value="${region.name}">${region.name}</option>`
            })
            document.getElementById("filterValue").innerHTML = html;
        })
    }else if ( e.target.value === "subRegion"){
        var html = `<option value="null">--select a value--</option>`
        fetch("/all-sub-regions").then(res=>res.json()).then(subRegions => {
            subRegions.forEach(subRegion => {
                html += `<option value="${subRegion.name}">${subRegion.name}</option>`
            })
            document.getElementById("filterValue").innerHTML = html;
        })
    }else if ( e.target.value === "population"){
        var html = `<option value="null">--select a value--</option>
                    <option value="bel1m">Below 1 Million</option>
                    <option value="1to10m">1 - 10 Million</option>
                    <option value="10to30m">10 - 30 Million</option>
                    <option value="30to100m">30 - 100 Million</option>
                    <option value="100to300m">100 - 300 Million</option>
                    <option value="300to500m">300 - 500 Million</option>
                    <option value="500to700m">500 - 700 Million</option>
                    <option value="700to1b">700 - 1 Billion</option>
                    <option value="gth1b">Greater Than 1 Billion</option>`;
        document.getElementById("filterValue").innerHTML = html;
    }else if ( e.target.value === "neighbours"){
        var html = `<option value="null">--select a value--</option>`
        fetch("/all-data").then(res=>res.json()).then(allCountries => {
            allCountries.forEach(country => {
                html += `<option value="${country.name}">${country.name}</option>`
            })
            document.getElementById("filterValue").innerHTML = html;
        })
    }resetDiffElem('sortBy')
}

document.getElementById("filterValue").oninput = function(e) {
    var filterBy = document.getElementById("filterBy").value;
    if (filterBy === 'region'){
        fetch(`/country-per?region=${e.target.value}`).then(res=>res.json()).then(countries => {
            document.getElementById("allTableData").value = JSON.stringify(countries); 
            document.getElementById("tableContent").innerHTML = getHTML(countries);
        })
    }else if (filterBy === 'subRegion'){
        fetch(`/country-per?subregion=${e.target.value}`).then(res=>res.json()).then(countries => {
            document.getElementById("allTableData").value = JSON.stringify(countries);
            document.getElementById("tableContent").innerHTML = getHTML(countries);
        })
    }else if (filterBy === 'neighbours'){
        fetch(`/country-per?neighbours=${e.target.value}`).then(res=>res.json()).then(countries => {
            document.getElementById("allTableData").value = JSON.stringify(countries);
            document.getElementById("tableContent").innerHTML = getHTML(countries);
        })
    }else if (filterBy === 'population'){
        fetch(`/country-per?population=${e.target.value}`).then(res=>res.json()).then(countries => {
            document.getElementById("allTableData").value = JSON.stringify(countries);
            document.getElementById("tableContent").innerHTML = getHTML(countries);
        })
    }resetDiffElem('sortBy')
}
document.getElementById("sortBy").oninput = function(e){
    var sortedTableData = new Array();
    if (e.target.value === "population"){
        sortedTableData = sorter(JSON.parse(document.getElementById("allTableData").value), 'population');
    }else if (e.target.value === "name") {
        sortedTableData = sorter(JSON.parse(document.getElementById("allTableData").value), 'name')
    }else if (e.target.value === "area") {
        sortedTableData = sorter(JSON.parse(document.getElementById("allTableData").value), 'area')
    }
    var html = getHTML(sortedTableData);
    document.getElementById("tableContent").innerHTML = html;
}