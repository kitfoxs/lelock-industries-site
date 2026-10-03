document.querySelectorAll('[data-menu-toggle]').forEach(button => {
  button.addEventListener('click', () => {
    const nav = document.getElementById(button.getAttribute('aria-controls'));
    const expanded = button.getAttribute('aria-expanded') === 'true';
    button.setAttribute('aria-expanded', String(!expanded));
    nav.classList.toggle('is-open', !expanded);
  });
});
const filters = document.querySelectorAll('[data-filter]');
filters.forEach(button => button.addEventListener('click', () => {
  filters.forEach(other => other.setAttribute('aria-pressed', String(other === button)));
  let count = 0;
  document.querySelectorAll('[data-project-kind]').forEach(card => {
    const show = button.dataset.filter === 'all' || card.dataset.projectKind === button.dataset.filter;
    card.hidden = !show;
    if (show) count += 1;
  });
  const output = document.getElementById('filter-result');
  if (output) output.textContent = `${count} project ${count === 1 ? 'family' : 'families'}`;
}));
