import nextpy as xt


def banner():
    return xt.fragment(
        xt.box(
            xt.image(
                src="/banner1.png",
                class_name="w-full h-96 sm:h-80 overflow-hidden object-cover object-bottom rounded-2xl bg-no-repeat",
            ),
            # xt.box(
            #     xt.box(
            #         xt.text(
            #             "The future of apps is ",
            #             xt.span(
            #                 "dot.agent",
            #                 class_name="bg-gradient-to-r from-[#660AB5] to-[#9F0FD2] bg-clip-text text-transparent",
            #             ),
            #             class_name="text-[#141718] font-[DMSans] h2 lg:text-5xl tracking-normal text-2xl md:text-3xl sm:leading-6 font-bold",
            #         ),
            #         xt.text(
            #             "Reimagine your digital life with dotagents—mini AI apps tailored to your needs.",
            #             class_name="text-[#141718] relative h2 md:text-2xl text-xl z-[99] font-medium font-[DMSans] lg:max-w-xl max-w-sm  my-2 leading-6 md:leading-8",
            #         ),
            #         xt.box(
            #             "Sign up for free",
            #             class_name="bg-white text-black w-44 rounded-md md:text-lg  font-[DMSans] text-xs  mt-8 py-3.5  px-4  font-bold h6",
            #         ),
            #         xt.image(
            #             src="/robort.png",
            #             class_name="lg:w-96 md:w-72 overflow-hidden  rotate-12 object-cover bg-no-repeat",
            #         ),
            #         #   background_image = "url('/banner1.png')",class_name ="w-full lg:h-96 h-80 overflow-hidden lg:p-16 p-8 sm:pl-8 lg:py-20 object-cover object-bottom rounded-2xl bg-no-repeat"
                 
                      
                
            #     ),   
            # ),
        #   class_name="absolute top-0 bottom-0 left-0 right-0 p-16 lg:p-8 sm:pl-8 py-20"
        ),
         class_name="relative overflow-hidden", 
    )
