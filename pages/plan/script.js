const planButtons = document.querySelectorAll('.select-plan');

planButtons.forEach((button, index) => {
  button.addEventListener('click', () => {
    const planDetails = [
      "Basic Plan: $10/month, 5 Users, 10 GB Storage",
      "Standard Plan: $30/month, 15 Users, 50 GB Storage",
      "Premium Plan: $60/month, Unlimited Users, 200 GB Storage"
    ];

    const contactPageURL = `http://www.zoserp.com/contact?message=${encodeURIComponent(planDetails[index])}`;
    window.location.href = contactPageURL;
  });
});
