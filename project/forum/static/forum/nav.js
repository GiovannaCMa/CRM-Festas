const links = document.querySelectorAll('.sidebar a');


links.forEach(link => {
  link.addEventListener('click', function() {
    
    links.forEach(l => l.classList.remove('active'));
    // deixa o bregueso marcado
    this.classList.add('active');

    localStorage.setItem('activeLink', this.href);
  });
});

window.addEventListener('load', () => {
  const activeLink = localStorage.getItem('activeLink'); //deixa marcado depois de atualizar a pagina
  if (activeLink) {
    links.forEach(link => {
      if (link.href === activeLink) {
        link.classList.add('active');
      }
    });
  }
});

