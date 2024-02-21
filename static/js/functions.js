document.addEventListener(
    "htmx:confirm",
    function (e) {
        if (e.detail.question !== null) {
            e.preventDefault();
            Swal.fire({
                // icon: "question",
                buttonsStyling: false,
                showCancelButton: true,
                reverseButtons: true,
                title: "Atenção!!!",
                text: `Tem certeza que deseja excluir o cadastro de ${(e.detail.question).toUpperCase()}?`,
                showClass: { popup: "animate__animated animate__fadeInUp animate__faster" },
                hideClass: { popup: "animate__animated animate__fadeOutDown animate__faster" },
            }).then(function (resultado) {
                if (resultado.isConfirmed) e.detail.issueRequest(true)
            })

        }
    }
)

function onClick(obj) {
    let editing = document.querySelector('.editing');

    if (editing) {
        htmx.trigger(editing, 'cancel')
    } else {
        htmx.trigger(obj, 'edit')
    }
}