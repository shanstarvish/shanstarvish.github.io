

document.querySelectorAll('.toggle').forEach(header => {
  header.addEventListener('click', () => {
      const details = header.nextElementSibling;

      // Toggle the 'details' section
      if (details.style.display === 'block') {
          details.style.display = 'none';
      } else {
          details.style.display = 'block';
      }
  });
});


