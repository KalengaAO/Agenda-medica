console.log("Agenda Médica carregada");


async function carregarAgenda(){

    const container = document.getElementById("appointments");


    try {

        const response = await fetch("/api/agendamentos");


        if (!response.ok){
            throw new Error("Erro ao buscar agenda");
        }


        const result = await response.json();


        const agendamentos = result.dados;


        container.innerHTML = "";


        agendamentos.forEach(item => {

            const card = document.createElement("div");

            card.className = "appointment";


            card.innerHTML = `

                <h3>
                    ${item.medico}
                </h3>

                <p>
                    Paciente:
                    ${item.paciente}
                </p>

                <p>
                    Especialidade:
                    ${item.especialidade}
                </p>

                <p>
                    Data:
                    ${item.data}
                    ${item.horario}
                </p>

                <p>
                    Convênio:
                    ${item.convenio}
                </p>

                <p>
                    Status:
                    ${item.status}
                </p>

            `;


            container.appendChild(card);

        });


    } catch(error){

        console.error(
            "Erro:",
            error
        );

        container.innerHTML =
        "<p>Erro ao carregar agenda.</p>";

    }

}


document.addEventListener(
    "DOMContentLoaded",
    carregarAgenda
);