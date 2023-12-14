export default {
  data() {
    return {
      firstName: '',
      lastName: '',
      userName: '',
      email: '',
      passwordSign: '',
      passwordSignConf: '',
    };
  },
  methods: {
    signUp() {
      // Add sign-up logic
      console.log('Sign Up:', this.firstName, this.lastName, this.userName, this.email, this.passwordSign, this.passwordSignConf);
    },
  },
};