console.log("Agenda Médica carregada");


async function loadAppointments() {

    const container = document.getElementById("appointments");

    if (!container) {
        return;
    }


    try {

        const response = await fetch(
            "http://localhost:5001/appointments"
        );


        if (!response.ok) {
            throw new Error(
                "Erro ao carregar agendamentos"
            );
        }


        const appointments = await response.json();


        container.innerHTML = "";


        appointments.forEach(item => {


            const card = document.createElement("div");

            card.className = "appointment";


            card.innerHTML = `

                <h3>${item.paciente}</h3>

                <p>
                    Médico:
                    ${item.medico}
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


    } catch(error) {

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
    loadAppointments
);