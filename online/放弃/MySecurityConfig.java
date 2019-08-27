package com.zlx.resume.config;

import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

//@EnableWebSecurity
public class MySecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    protected void configure(HttpSecurity http) throws Exception {
//        super.configure(http);

        //        定制请求的授权规则
        http.authorizeRequests().antMatchers("/").permitAll()
                .antMatchers("/leve1/**").hasRole("admin")
                .antMatchers("/leve2/**").hasRole("companyuser")
                .antMatchers("/leve3/**").hasRole("user");

//        开启自定配置的登录功能，如果没有权限就会来到登录页面，不会返回403
        http.formLogin();
//      /login  来到登录页
//        /login?error 登录错误会来到这个页面，表示登陆失败

        //开启自动配置的注销功能
        //访问loginout，注销用户，清除session
        //注销成功会返回login？logout页面
        http.logout().logoutSuccessUrl("/");

    }

    //定义认证规则
    @Override
    protected void configure(AuthenticationManagerBuilder auth) throws Exception {
//        super.configure(auth);
        auth.inMemoryAuthentication().passwordEncoder(new BCryptPasswordEncoder())
                .withUser("zlx").password(new BCryptPasswordEncoder().encode("zlx") ).roles("admin")
                .and()
                .withUser("xx").password(new BCryptPasswordEncoder().encode("xx")).roles("companyuser")
                .and()
                .withUser("yy").password(new BCryptPasswordEncoder().encode("yy")).roles("user");

    }
}
