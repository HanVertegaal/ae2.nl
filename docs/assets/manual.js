/* Keep chapter navigation expanded on desktop and compact on small screens. */
function updateManualNavigation(event)
{
  const menu = document.querySelector('.chapter-menu');
  if (menu)
  {
    menu.open = !event.matches;
  }
}

/* Set the initial menu state and respond when the layout breakpoint changes. */
function initializeManualNavigation()
{
  const mobileViewport = window.matchMedia('(max-width: 760px)');
  updateManualNavigation(mobileViewport);
  mobileViewport.addEventListener('change', updateManualNavigation);
}

initializeManualNavigation();
