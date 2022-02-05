const weatherView = document.querySelector('.weather')
const weatherForm = document.querySelector('#weather-form')
const cityInput = document.querySelector('#city-input')

const fetchWeather = async (city) => {
    const url = `http://localhost:5000/api?q=${city}`
    const request = new Request(url, {
        method: "GET",
    })

    const res = await fetch(request)
    const data = await res.json()

    if (data.cod === '404') {
        alert('City not found.')
        return
    }

    if (data.cod === 401) {
        alert('Invalid API Key.')
        return
    }

    const weather = {
        city: data.name,
        temp: kelvinToFahrenheit(data.main.temp),
    }

    displayWeather(weather)
}

const displayWeather = (data) => {
    weatherView.innerHTML = `
    <h1>Weather in ${data.city}</h1>
    <h2>${data.temp} &deg;F</h2>
  `
    cityInput.value = ''
}

const kelvinToFahrenheit = (temp) => {
    return Math.ceil(((temp - 273.15) * 9) / 5 + 32)
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
fetchWeather('Miami')