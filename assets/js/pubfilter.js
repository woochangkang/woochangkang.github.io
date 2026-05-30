// Publications topic filter + deep-link support.
// Kept in an external file so Jekyll/kramdown never markdown-processes it.
(function () {
  var wrap = document.getElementById('topicFilter');
  if (!wrap) return;

  function apply(topic) {
    var chips = wrap.querySelectorAll('.chip');
    for (var i = 0; i < chips.length; i++) {
      var c = chips[i];
      if (c.getAttribute('data-topic') === topic) {
        c.classList.add('is-active');
      } else {
        c.classList.remove('is-active');
      }
    }
    var items = document.querySelectorAll('.pub');
    for (var j = 0; j < items.length; j++) {
      var li = items[j];
      var tags = (li.getAttribute('data-tags') || '').split('|');
      var show = (topic === 'all' || tags.indexOf(topic) >= 0);
      li.style.display = show ? '' : 'none';
    }
  }

  wrap.addEventListener('click', function (e) {
    var b = e.target.closest ? e.target.closest('.chip') : null;
    if (b) apply(b.getAttribute('data-topic'));
  });

  // Deep link from the Research page, e.g. /publications/#topic=Polarization
  function fromHash() {
    var m = (location.hash || '').match(/topic=([^&]+)/);
    if (!m) return;
    var t = decodeURIComponent(m[1]);
    var chips = wrap.querySelectorAll('.chip');
    for (var i = 0; i < chips.length; i++) {
      if (chips[i].getAttribute('data-topic') === t) {
        apply(t);
        chips[i].scrollIntoView({ block: 'nearest' });
        return;
      }
    }
  }
  fromHash();
  window.addEventListener('hashchange', fromHash);
})();
