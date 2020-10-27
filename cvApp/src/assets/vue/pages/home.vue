<template>
  <f7-page>
    <f7-navbar>
      <div class="title">Building Recognizer</div>
    </f7-navbar>
    <f7-block-title class="searchbar-found">Options</f7-block-title>
    <f7-list class="components-list searchbar-found">
      <f7-list-item link="/identify/" title="Identify" panel-close>
        <f7-icon slot="media" class="f7-icons">camera_fill</f7-icon>
      </f7-list-item>
      <f7-list-item link="/choose/" title="Choose..." panel-close>
        <f7-icon slot="media" class="f7-icons">photo</f7-icon>
      </f7-list-item>
    </f7-list>
  </f7-page>
</template>
<script>
export default {
  components: {},
};
</script>
