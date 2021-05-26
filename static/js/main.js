import {dataHandler} from "./dataHandler.js";

let headers = document.getElementsByTagName('th')
for (let header of headers) {
    header.addEventListener('click', function () {
        sortBy(header.id)
    })
}


function sortBy(headerID) {
    let currentHeader = document.getElementById(headerID)
    iAmTheOnlyOne()
    setOrderSymbol()

    function setOrderSymbol() {
        if (currentHeader.innerText.includes('⇩')) {
            currentHeader.innerText = currentHeader.innerText.substr(0, currentHeader.innerText.length - 1) + '⇧'
            sortContents(currentHeader.innerText)
        } else if (currentHeader.innerText.includes('⇧')) {
            currentHeader.innerText = currentHeader.innerText.substr(0, currentHeader.innerText.length - 1) + '⇩'
            sortContents(currentHeader.innerText)
        } else {
            currentHeader.innerText = currentHeader.innerText + '⇩'
            sortContents(currentHeader.innerText)
        }
    }


    function iAmTheOnlyOne() {
        for (let header of headers) {
            if (header.id !== headerID && header.innerText.includes('⇧') || header.id !== headerID && header.innerText.includes('⇩')) {
                header.innerText = header.innerText.substr(0, header.innerText.length - 1)
            }
        }
    }

    function sortContents(argument) {
        let orderDirection
        let orderCriteria = headerID.substr(7, headerID.length)
        let currentPage = window.location.href.substr(39, window.location.href.length - 1)
        if (argument[argument.length - 1] === '⇩') {
            orderDirection = 'ASC'
        } else {
            orderDirection = 'DESC'
        }

        let dataToPost = [currentPage, orderCriteria, orderDirection]

        dataHandler._api_post('http://127.0.0.1:5000/shows/most-rated/' + currentPage, dataToPost,
            function (withDataReceived) {
                transformTable(withDataReceived)
            })
    }
}


function transformTable(withDataReceived) {
    let rows = document.querySelectorAll('tr')
    let index = 0
    let j = 0
    let orderItems = ['title', 'date_part', 'runtime', 'rating', 'genre', 'homepage', 'trailer']
    console.log(withDataReceived[0])
    for (let row of rows) {
        if (index === 0) {
            index++
        } else {
            let cells = row.querySelectorAll('td')
            for (let cell of cells) {
                if (orderItems[j] === 'rating'){
                    cell.innerText = withDataReceived[index - 1][orderItems[j]].substring(0,3)
                }else if (orderItems[j] === 'homepage'){
                    cell.link.href = withDataReceived[index - 1][orderItems[j]]
                }else
                cell.innerText = withDataReceived[index - 1][orderItems[j]]
                j++
            }
            j = 0
            index+=1
        }
    }

}