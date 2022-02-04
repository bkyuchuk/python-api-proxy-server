const weather = document.querySelector(".weather")
const form = document.querySelector("#weather-form")
const cityInput = document.querySelector("#city-input")

form.addEventListener('submit', (e) => {
    e.preventDefault()

    if (cityInput.value === "") {
        alert("Please enter a city.")
    } else {
        fetchWeather(cityInput.value)
    }
})

const fetchWeather = async (city) => {
    const url = `/api?q=${city}`

    const res = await fetch(url)
    const data = await res.json()


    if (data.cod === 404) {
        alert("City not found.")
        return
    }

    if (data.cod === 401) {
        alert("Invalid API key.")
        return
    }

    const weather = {
        city: data.name,
        temp: kelvinToCelcius(data.main.temp)
    }

    displayWeather(weather)
}

const kelvinToCelcius = (temp) => {
    return Math.ceil(temp - 273.15)
}

const displayWeather = (data) => {
    weather.innerHTML = `
    <h1>Weather in ${data.city}</h1>
    <h2>${data.temp} &deg;C</h2>
    `
}

// Initial fetch
fetchWeather("Sofia")