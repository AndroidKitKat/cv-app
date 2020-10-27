// Require Cordova plugin : cordova-plugin-camera

<template>
  <f7-page>
      <f7-navbar title="Identify" back-link="Back"></f7-navbar>
      <img style="width: 100%" v-if="imagePath !== ''" :src="imagePath" />
      <f7-button class="button-outline-ios" @click="takePicture">{{ btnTitle }}</f7-button>
      <f7-button class="button-outline-ios" @click="sendPicture" v-if="btnTitle === 'Retake photo'">Submit</f7-button>
  </f7-page>
</template>
<script>
import { nativeAlert } from "../../libs/index";

export default {
  components: {},
  data() {
    return {
      imagePath: "",
      btnTitle: "Take photo",
    };
  },
  methods: {
    takePicture: function () {
      if (navigator.camera) {
        navigator.camera.getPicture(this.setPicture, this.error, {
          destinationType: Camera.DestinationType.DATA_URL,
        });
      } else {
        // If the navigator.camera is not available display generic error to the user.
        this.error();
      }
    },
    setPicture(imageData) {
      this.imagePath = "data:image/jpeg;base64," + imageData
      this.btnTitle = "Retake photo"
    },
    error() {
      nativeAlert("this is the sad");
    },
  },
  // lifecycle hooks
};
</script>