<template>
  <div class="p-5 h-screen bg-gray-100">
    <div class=" flex justify-between items-center">
      <h1 class="text-3xl font-bold justify-center flex justify-items-center p-4">Support Tickets</h1>
      <ErrorMessage :message="newticket.error" />
    
    
      <Button @click="dialog2 = true" variant="solid" class="p-4 ">
        New Ticket
      </Button>
      <Dialog v-model="dialog2" >
        <template #body-title>
          <h3>Custom Title</h3>
        </template>
        <template #body-content>
          <div class="p-2 space-y-4">
            <FormControl
                :type="'text'"
                size="sm"
                variant="subtle"
                placeholder="Title"
                :disabled="false"
                label="Title"
                v-model="titleInputValue"
                
              />
            <FormControl
                 :type="'date'"
                 size="sm"
                 variant="subtle"
                 placeholder="Placeholder"
                 :disabled="false"
                 label="Date"
                 v-model="dateInputValue"
            />

            <FormControl
                   :type="'textarea'"
                   size="sm"
                   variant="subtle"
                   placeholder="Placeholder"
                   :disabled="false"
                   label="Label"
                   v-model="descriptionInputValue"
            />
            <select class="w-full p-2 border-2 border-gray-200 rounded-md" v-model="categoryInputValue">
              <option value="Paper Quality">Paper Quality</option>
              <option value="Delivery">Delivery</option>
              <option value="Other">Other</option>
            </select>
            
          </div>
          
        </template>
        <template #actions>
          <Button variant="solid"
            @click="handleSubmit"
          >
            Confirm
          </Button>
          <Button
            class="ml-2"
            @click="dialog2 = false"
          >
            Close
          </Button>
        </template>
      </Dialog>
      
    </div>
  
    <table class="w-full">
      <thead class="bg-gray-50 border-b-2 border-gray-200">
        <tr>
          <th class="p-3 text-sm font-semibold tracking-wide text-left">Title</th>
          <th class="p-3 text-sm font-semibold tracking-wide text-left">Status</th>
          <th class="p-3 text-sm font-semibold tracking-wide text-left">Category</th>
          
        </tr>
      </thead>
      
      <tbody class="border-b-2 border-gray-200 bg-white">
        <tr v-for="ticket in ticket" :key="ticket.name">
          <td class="border-2 p-3 text-sm text-gray-800">{{ ticket.title }}</td>
          <td class="border-2  p-2 flex justify-center items-center">
            <Transition :show="showBadge" mode="out-in">  <!-- Added Transition -->
              <Badge 
                :class="{
                  'bg-red-500': ticket.status === 'Open',
                  'bg-yellow-500': ticket.status === 'Waiting for reply',
                  'bg-green-500': ticket.status === 'Closed'
                }"
                class="border-2 p-6 w-full flex justify-center items-center text-sm text-center text-white"  
              >
                {{ ticket.status }}
              </Badge>
            </Transition>
          </td>
          <td class="border-2  text-sm text-gray-800">{{ ticket.category }}</td>
        </tr>
        
      </tbody>
      
    </table>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { createListResource, createResource } from 'frappe-ui';
import { Badge, Dialog, FormControl, ErrorMessage } from 'frappe-ui';


const tickets = createListResource({
  doctype: 'Support Ticket',
  fields: ['title', 'status', 'category'],
  auto: true
});

const ticket = computed(() => {
  if (tickets.list.data) {
    return tickets.list.data;
  }
});
const titleInputValue = ref('');
const dateInputValue = ref('');
const descriptionInputValue = ref('');
const categoryInputValue = ref('');
const dialog2 = ref(false); // Added showBadge variable
const showBadge = ref(true); // Added showBadge variable

const newticket = createResource({
   url: 'store.api.newticket',
  
   makeParams(){
      return {
        data: {
        title: titleInputValue.value,
        purchase_date: dateInputValue.value,
        description: descriptionInputValue.value,
        status: 'Open',
        category: categoryInputValue.value
        }
      }
   }
});

const handleSubmit = async () => {
  try {
    await newticket.submit();
   
    titleInputValue.value = '';
    dateInputValue.value = '';
    descriptionInputValue.value = '';
    categoryInputValue.value = '';
    // Close the dialog
    dialog2.value = false;
  } catch (error) {
    // Handle errors (e.g., display an error message)
    console.error('Error creating ticket:', error);
  }
};
</script>
