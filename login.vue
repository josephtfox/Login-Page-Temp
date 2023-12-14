export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    login() {
      // Add login logic
      console.log('Login:', this.username, this.password);
    },
  },
};