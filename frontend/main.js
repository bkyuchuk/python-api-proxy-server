const weatherView = document.querySelector('.weather')
const weatherForm = document.querySelector('#weather-form')
const cityInput = document.querySelector('#city-input')

// TODO: Change this before deployment.
BASE_URL = "http://localhost:5000"

const fetchWeather = async (city) => {
    const url = `${BASE_URL}/api?q=${city}`
    const request = new Request(url, {
        method: "GET",
    })

    const res = await fetch(request)
    const data = await res.json()

    if (res.status != 200) {
        alert(errors[res.status])
        return
    }

    const weather = {
        city: data.name,
        temp: kelvinToCelcius(data.main.temp),
    }

    displayWeather(weather)
}

errors = {
    404: "City not found.",
    401: "Invalid API key.",
    429: "Requests limit exceeded."
}

const displayWeather = (data) => {
    weatherView.innerHTML = `
    <h1>Weather in ${data.city}</h1>
    <h2>${data.temp} &deg;C</h2>
  `
    cityInput.value = ''
}

const kelvinToCelcius = (temp) => {
    return Math.ceil(temp - 273.15);
}

weatherForm.addEventListener('submit', (e) => {
    e.preventDefault()

    if (cityInput.value === '') {
        alert('Please enter a city.')
    } else {
        fetchWeather(cityInput.value)
    }
})

// Initial fetch
fetchWeather('Berlin')