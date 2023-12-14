export default {
    methods: {
      toggleForm() {
        // Toggle between /login and /signup routes
        const nextRoute = this.$route.path === '/login' ? '/signup' : '/login';
        this.$router.push(nextRoute);
      },
    },
  };