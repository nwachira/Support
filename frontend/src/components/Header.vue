<template>
    <div class="flex justify-between items-center p-6 m-2 shadow shadow-blue-400/50">
      <img src="/public/Screenshot from 2024-06-30 14-04-53.png" 
        class="h-12 w-12 cursor-pointer"
        alt="">
      <Dropdown v-if="session.isLoggedIn"
        class="cursor-pointer"
        :options="[
          {
            label: `${session.user}`, // Use template literal for interpolation
          },
          {
            label: 'Switch to Desk',
            onClick: () => {
              router.push('/desk');
            }
          },
          {
            label: 'Logout',
            onClick: () => {
              session.logout.submit(); // Call the logout function
            }
          }
        ]"
        :button="{
          label: 'Actions',
        }"
      >
        <Avatar
          :shape="'square'"
          image="https://i.pravatar.cc/100"
          label="EY"
          size="2xl"
        />
      </Dropdown>
      
    </div>
  </template>
  
  <script setup>
    import { Dropdown, Avatar } from 'frappe-ui';
    import { useRouter } from 'vue-router';
    import { session } from '../data/session';
  
    const router = useRouter();
  </script>
  