// ...existing code...
const emailInput = document.getElementById('email')
const senhaInput = document.getElementById('senha')
const btn = document.querySelector('.btn-primary');

const usuario = {
  email: 'felipesalva@gmail.com',
  senha: 'JGlacrou'
};

if (!btn) {
  console.error('Botão .btn-primary não encontrado');
}

btn.addEventListener('click', (e) => {
  e.preventDefault();
  const emailValor = (emailInput.value || '').trim().toLowerCase();
  const senhaValor = (senhaInput.value || '').trim();

  if (emailValor === usuario.email.toLowerCase() && senhaValor === usuario.senha) {
    window.location.href = '../../finanças/financas.html';
  } else {
    alert('Email e/ou senha incorreto');
  }
});
// ...existing code...