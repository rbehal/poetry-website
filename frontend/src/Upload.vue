<template>
    <div class="row">
        <div class="col" style="text-align: center">
            <h1>Upload Page</h1>
            <form action="http://127.0.0.1:6001/upload" method="POST" enctype="multipart/form-data">
                <b-form-file 
                    v-model="file" 
                    class="py-2" 
                    accept="application/pdf"
                    name="poems"
                    plain
                >
                </b-form-file>
                <b-button 
                    type="submit" 
                    variant="info"
                    class="upload-button"
                >
                    Upload
                </b-button>
            </form>
        </div>
    </div>
</template>

<script>
import 'bootstrap-vue/dist/bootstrap-vue.css'

export default {

}
</script>

<style> 
.upload-button {
    margin-top: 1%;
    margin-bottom: 1%;
    height: 50px;
    width: 150px;
}
</style>