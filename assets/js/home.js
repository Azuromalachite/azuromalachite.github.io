const toggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('.site-nav');
function closeNavigation() {
  navigation.classList.remove('is-open');
  toggle.setAttribute('aria-expanded', 'false');
  toggle.textContent = 'Menu +';
}
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  navigation.classList.toggle('is-open', open);
  toggle.setAttribute('aria-expanded', String(open));
  toggle.textContent = open ? 'Close −' : 'Menu +';
});
document.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && toggle.getAttribute('aria-expanded') === 'true') {
    closeNavigation(); toggle.focus();
  }
});
navigation.addEventListener('click', (event) => {
  if (event.target.closest('a')) closeNavigation();
});
window.matchMedia('(min-width: 861px)').addEventListener('change', closeNavigation);
