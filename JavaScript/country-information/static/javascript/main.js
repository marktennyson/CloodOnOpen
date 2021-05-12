const getTableHTML = (countries) => {
    var html  =new String();
    countries.forEach((country, counter) =>{
        html += `<tr>
            <td class="px-6 py-4 whitespace-nowrap">
                <div class="text-sm text-gray-900">${counter+1}</div>
            </td>
            <td class="px-6 py-4 whitespace-nowrap">
                <div class="flex items-center">
                    <div class="flex-shrink-0 h-10 w-10">
                        <img class="h-10 w-10 rounded-full" src="${country.flag}" alt="">
                    </div>
                </div>
            </td>
            <td class="px-3 py-2 ">
                <div class="text-sm text-gray-900">${country.name}</div>
            </td>
            <td class="px-3 py-2 ">
            <div class="text-sm text-gray-900">${country.capital}</div>
            </td>
            <td class="px-3 py-2 whitespace-nowrap">
                <div class="text-sm text-gray-900">${country.region}</div>
            </td>
            <td class="px-3 py-2 whitespace-nowrap">
                <div class="text-sm text-gray-900">${country.subRegion}</div>
            </td>
            <td class="px-3 py-2 whitespace-nowrap">
                <div class="text-sm text-gray-900">${country.population}</div>
            </td>
            <td class="px-3 py-2 whitespace-nowrap">
                <div class="text-sm text-gray-900">${country.languages}</div>
            </td>
            <td class="px-3 py-2 whitespace-nowrap">
                <div class="text-sm text-gray-900">${country.currency}</div>
            </td>
            <td class="px-3 py-2 whitespace-nowrap">
                <div class="text-sm text-gray-900">${country.code}</div>
            </td>
        </tr>`
    });return html;
}
const getDropdownHtml = (options) => {
    let dropdownJs = new String();
    options.forEach(option => {
        dropdownJs += `
            <div class="py-1" role="none">
            <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">${option}</a>
            </div>`
    })
    return dropdownJs;
}
const filterByDropdown = () => {
    flag = document.getElementById("filterByData").value;
    options = ['region', 'sub region', 'population', 'neighbours']
    // options = ['Asia', 'Europe', 'Africa', 'Americas', 'Oceania', 'Polar', 'no-region']
    if (flag === "false") {
        document.getElementById("filterByData").innerHTML = getDropdownHtml(options);
        document.getElementById("filterByData").value = "true";
    }else{
        document.getElementById("filterByData").innerHTML = "";
        document.getElementById("filterByData").value = "false";
    }
}


window.onload = () =>{
    fetch("https://restcountries.eu/rest/v2/all").then(res=>res.json()).then(countries=>{
        document.getElementById("tableData").innerHTML = getTableHTML(countries);
    })
} 