const getHTML = (countries) => {
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

window.onload = () =>{
    fetch("/all-data").then(res=>res.json()).then(countries=>{
        document.getElementById("tableData").innerHTML = getHTML(countries);
    })
} 