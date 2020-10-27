// Require Cordova plugin : cordova-plugin-camera

<template>
  <f7-page>
    <f7-navbar title="Choose" back-link="Back"></f7-navbar>
    <img style="width: 100%" v-if="imagePath !== ''" :src="imagePath" />
    <f7-button class="button-outline-ios" @click="takePicture">{{
      btnTitle
    }}</f7-button>
    <f7-button
      class="button-outline-ios"
      @click="sendPicture"
      v-if="btnTitle === 'Take different photo'"
      >Submit</f7-button
    >
    {{ dater }}
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
      dater: "",
      imageBase64: "",
    };
  },
  methods: {
    takePicture: function () {
      if (navigator.camera) {
        navigator.camera.getPicture(this.setPicture, this.error, {
          quality: 50,
          destinationType: Camera.DestinationType.DATA_URL,
          encodingType: Camera.EncodingType.JPEG,
          sourceType: Camera.PictureSourceType.CAMERA,
          mediaType: Camera.MediaType.PICTURE
        });
      } else {
        // If the navigator.camera is not available display generic error to the user.
        this.error();
      }
    },
    setPicture: function (imageData) {
      this.imagePath = "data:image/jpeg;base64," + imageData;
      this.btnTitle = "Take different photo";
    },
    error: function () {
      nativeAlert("this is the sad");
    },
    sendPicture: function () {
      var body = {
        picture: this.imagePath
      }
      fetch("http://10.18.16.48:8008/identify", {
        method: "PUT",
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(body),
      }).then(res => res.text()).then(data => this.dater = data)
    },
  },
};
</script>