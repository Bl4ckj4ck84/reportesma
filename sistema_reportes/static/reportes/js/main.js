document.addEventListener('DOMContentLoaded', () => {
    const organismosList = document.getElementById('organismos-list');
    const ppdaList = document.getElementById('ppda-list');
    const medidasList = document.getElementById('medidas-list');

    // Función para cargar datos de la API
    async function fetchData(url, targetElement) {
        try {
            const response = await fetch(url, {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('token') // Si necesitas autenticación
                }
            });
            if (!response.ok) throw new Error('Error al cargar datos');
            const data = await response.json();
            targetElement.innerHTML = JSON.stringify(data, null, 2);
        } catch (error) {
            targetElement.innerHTML = `<p>Error: ${error.message}</p>`;
        }
    }

    // Cargar Organismos Sectoriales
    document.getElementById('fetch-organismos').addEventListener('click', () => {
        fetchData('/api/organismos-sectoriales/', organismosList);
    });

    // Cargar Planes PPDA
    document.getElementById('fetch-ppda').addEventListener('click', () => {
        fetchData('/api/planes-ppda/', ppdaList);
    });

    // Cargar Medidas de Avance
    document.getElementById('fetch-medidas').addEventListener('click', () => {
        fetchData('/api/medidas-avance/', medidasList);
    });
});