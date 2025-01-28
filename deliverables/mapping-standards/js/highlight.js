window.addEventListener('load', () => {
  document.querySelectorAll('pre.cypher').forEach(pre => {
    pre.classList.add("cm-s-default")
    CodeMirror.runMode(pre.children[0].textContent,"cypher",pre)
  })
  document.querySelectorAll('pre.ttl').forEach(pre => {
    pre.classList.add("cm-s-default")
    CodeMirror.runMode(pre.children[0].textContent,"turtle",pre)
  })
  document.querySelectorAll('pre.sparql').forEach(pre => {
    pre.classList.add("cm-s-default")
    CodeMirror.runMode(pre.children[0].textContent,"sparql",pre)
  })
})
