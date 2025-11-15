const links = document.querySelectorAll('.menu .menu-item');

if (links.length) {
  const extractSection = (path) => {
    if (!path) return '';
    const cleanPath = new URL(path, window.location.origin).pathname;
    const [section] = cleanPath.split('/').filter(Boolean);
    return section || '';
  };

  const explicitSection = document.body?.dataset?.section;
  const storedSection = localStorage.getItem('activeSection');
  const currentSection =
    explicitSection ||
    extractSection(window.location.pathname) ||
    storedSection ||
    'home';

  links.forEach((link) => {
    const linkSection = link.dataset.section || extractSection(link.href);
    const isActive = currentSection === linkSection;
    link.classList.toggle('active', isActive);

    link.addEventListener('click', () => {
      localStorage.setItem('activeSection', linkSection);
    });
  });
}