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
    const error = JSON.parse(evt.detail.xhr.responseText);
    showToast(error.detail);
});

function showToast(msg) {
    const toast = document.getElementById('toast');
    toast.innerHTML = msg;
    toast.classList.add('show', 'animate__fadeInUp');
    setTimeout(function () { toast.classList.remove('show', 'animated__fadeInUp') }, 3000);
};

function showDetail() {
    const detalhe = document.getElementById('detalhe');
    const info = document.getElementById('info');
    detalhe.classList.add('show');
    info.classList.add('show', "animate__fadeInUp")

}

function hideDetail() {
    const detalhe = document.getElementById('detalhe');
    const info = document.getElementById('info');
    detalhe.classList.remove('show');
    info.classList.remove('show', "animate__fadeInUp")

}

function onClick(obj) {
    let editing = document.querySelector('.editing');

    if (editing) {
        htmx.trigger(editing, 'cancel')
    } else {
        htmx.trigger(obj, 'edit')
    }
}
