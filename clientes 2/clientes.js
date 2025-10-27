// ===== MENU ATIVO =====
const links = document.querySelectorAll('.menu-item');
links.forEach(link => {
  link.addEventListener('click', function () {
    links.forEach(l => l.classList.remove('active'));
    this.classList.add('active');
    localStorage.setItem('activeLink', this.textContent.trim());
  });
});

window.addEventListener('load', () => {
  const active = localStorage.getItem('activeLink');
  if (active) {
    links.forEach(link => {
      if (link.textContent.trim() === active) {
        link.classList.add('active');
      }
    });
  }
});

// ===== MODAL DE EDIÇÃO =====
const modal = document.getElementById('modal');
const editarBtn = document.getElementById('editarBtn');
const cancelarBtn = document.getElementById('cancelarBtn');
const formEditar = document.getElementById('formEditar');

editarBtn.addEventListener('click', () => {
  document.getElementById('editNome').value = document.getElementById('nomeCliente').textContent;
  document.getElementById('editNascimento').value = "2006-05-30"; // formato ISO
  document.getElementById('editEmail').value = document.getElementById('email').textContent;
  document.getElementById('editSexo').value = document.getElementById('sexo').textContent;
  document.getElementById('editCpf').value = document.getElementById('cpf').textContent;
  document.getElementById('editRg').value = document.getElementById('rg').textContent;
  document.getElementById('editOrigem').value = document.getElementById('comoConheceu').textContent;

  modal.style.display = 'flex';
});

cancelarBtn.addEventListener('click', () => {
  modal.style.display = 'none';
});

formEditar.addEventListener('submit', e => {
  e.preventDefault();

  document.getElementById('nomeCliente').textContent = document.getElementById('editNome').value;
  document.getElementById('nascimento').textContent = new Date(document.getElementById('editNascimento').value).toLocaleDateString('pt-BR');
  document.getElementById('email').textContent = document.getElementById('editEmail').value;
  document.getElementById('email').href = `mailto:${document.getElementById('editEmail').value}`;
  document.getElementById('sexo').textContent = document.getElementById('editSexo').value;
  document.getElementById('cpf').textContent = document.getElementById('editCpf').value;
  document.getElementById('rg').textContent = document.getElementById('editRg').value;
  document.getElementById('comoConheceu').textContent = document.getElementById('editOrigem').value;

  modal.style.display = 'none';
});
