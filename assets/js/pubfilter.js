// Publications: group tabs (English / Korean / Working / Grants) + topic
// filter applied within the active tab + deep-link support (#topic=...).
// External file so Jekyll/kramdown never markdown-processes it.
(function () {
  var tabsWrap = document.getElementById('pubTabs');
  if (!tabsWrap) return;
  var filterWrap = document.getElementById('topicFilter');

  var sections = {};
  Array.prototype.forEach.call(document.querySelectorAll('.pub-tab'), function (s) {
    sections[s.getAttribute('data-tab')] = s;
  });

  var state = { tab: 'english', topic: 'all' };

  function pubsIn(tab) {
    var s = sections[tab];
    return s ? s.querySelectorAll('.pub') : [];
  }
  function tabHasMatches(tab, topic) {
    var pubs = pubsIn(tab);
    if (!pubs.length) return false;            // wip / grants
    if (topic === 'all') return true;
    for (var i = 0; i < pubs.length; i++) {
      if ((pubs[i].getAttribute('data-tags') || '').split('|').indexOf(topic) >= 0) return true;
    }
    return false;
  }
  function applyTopic(tab, topic) {
    Array.prototype.forEach.call(pubsIn(tab), function (li) {
      var tags = (li.getAttribute('data-tags') || '').split('|');
      li.style.display = (topic === 'all' || tags.indexOf(topic) >= 0) ? '' : 'none';
    });
  }
  function render() {
    Object.keys(sections).forEach(function (t) { sections[t].hidden = (t !== state.tab); });
    Array.prototype.forEach.call(tabsWrap.querySelectorAll('[data-tab]'), function (b) {
      b.classList.toggle('is-active', b.getAttribute('data-tab') === state.tab);
    });
    var hasPubs = pubsIn(state.tab).length > 0;
    if (filterWrap) {
      filterWrap.style.display = hasPubs ? '' : 'none';
      Array.prototype.forEach.call(filterWrap.querySelectorAll('.chip'), function (c) {
        c.classList.toggle('is-active', c.getAttribute('data-topic') === state.topic);
      });
    }
    applyTopic(state.tab, state.topic);
  }
  function setTab(tab) { state.tab = tab; render(); }
  function setTopic(topic) {
    state.topic = topic;
    if (!tabHasMatches(state.tab, topic)) {        // jump to a tab that has matches
      var order = ['english', 'korean'];
      for (var i = 0; i < order.length; i++) {
        if (tabHasMatches(order[i], topic)) { state.tab = order[i]; break; }
      }
    }
    render();
  }

  tabsWrap.addEventListener('click', function (e) {
    var b = e.target.closest('[data-tab]');
    if (b) setTab(b.getAttribute('data-tab'));
  });
  if (filterWrap) filterWrap.addEventListener('click', function (e) {
    var c = e.target.closest('.chip');
    if (c) setTopic(c.getAttribute('data-topic'));
  });

  function fromHash() {
    var m = (location.hash || '').match(/topic=([^&]+)/);
    if (m) setTopic(decodeURIComponent(m[1]));
  }
  render();
  fromHash();
  window.addEventListener('hashchange', fromHash);
})();
