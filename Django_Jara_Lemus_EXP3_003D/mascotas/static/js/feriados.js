(
  async () =>{
    try {
    let response = await fetch(`https://apis.digital.gob.cl/fl/feriados/2023`, {
    });
    response = await response.json();
    let datos = response.data

    insertarDatos = document.getElementById('data')
    for(let i=0; i < datos.length; i++){
      insertarDatos.innerHTML+=`
              <tr>
                <td><p class="texto">${datos[i].date}</p></td>
                <td><p class="texto1">${datos[i].title}</p></td>
                <td><p class="texto2">${datos[i].type}</p></td>
                <td><p class="texto3">${datos[i].extra}</p></td>
              </tr>
        `

                    
        }

    
  } catch (error) {
    console.error(error);
  }
  });

