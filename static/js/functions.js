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
);

document.addEventListener('htmx:responseError', evt => {
    const elm = document.getElementById('toast');
    error = JSON.parse(evt.detail.xhr.responseText);
    elm.innerHTML = error.detail;
    elm.classList.add('show', 'animate__fadeInUp');
    setTimeout(function () { elm.classList.remove('show', 'animated__fadeInUp') }, 3000);
});

function onClick(obj) {
    let editing = document.querySelector('.editing');

    if (editing) {
        htmx.trigger(editing, 'cancel')
    } else {
        htmx.trigger(obj, 'edit')
    }
}