<template>
  <div class="row">
    <div class="col" style="text-align: center">
      <h1>Upload Page</h1>
      <form
        action="http://18.118.168.240:5000/upload"
        method="POST"
        enctype="multipart/form-data"
      >
        <b-form-file
          class="py-2"
          accept="application/pdf"
          name="poems"
          v-model="file"
          plain
        >
        </b-form-file>
        <b-button
          type="submit"
          variant="info"
          class="upload-button"
          :disabled="!isFile()"
        >
          Upload
        </b-button>
      </form>
    </div>
  </div>
</template>

<script>
import "bootstrap-vue/dist/bootstrap-vue.css";

export default {
  data: function () {
    return {
      file: null,
    };
  },
  methods: {
    isFile: function () {
      if (this.file == null) return false;
      return true;
    },
  },
};
</script>

<style>
.upload-button {
  margin-top: 1%;
  margin-bottom: 1%;
  height: 50px;
  width: 150px;
}
</style>
